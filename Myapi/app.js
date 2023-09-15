require('dotenv').config();
const express = require("express");
const bodyParser = require("body-parser");
const pgp = require("pg-promise")();

const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());

const db = pgp(process.env.DATABASE_URL, {
  ssl: { rejectUnauthorized: false }, // Disable SSL certificate verification for development/testing
});

const createTableQuery = `
  CREATE TABLE IF NOT EXISTS Persons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
  )
`;

// Create the 'Persons' table if it does not exist
db.none(createTableQuery)
  .then(() => {
    console.log("Table 'Persons' created (if not exists)");
  })
  .catch((error) => {
    console.error("Error creating table 'Persons':", error);
  });

// Get a person by ID or Name
app.get("/api/persons/:param", (req, res) => {
  const param = req.params.param;

  if (!isNaN(param)) {
    // If param is numeric, assume it's an ID
    const personId = parseInt(param);

    db.oneOrNone("SELECT * FROM Persons WHERE id = $1", [personId])
      .then((result) => {
        if (result) {
          return res.json(result);
        }
        return res.status(404).json({ error: "Person not found" });
      })
      .catch((err) => {
        console.error(err);
        return res.status(500).json({ error: "Database error" });
      });
  } else {
    // If param is not numeric, assume it's a Name
    db.manyOrNone("SELECT * FROM Persons WHERE name = $1", [param])
      .then((result) => {
        if (result.length > 0) {
          return res.json(result);
        }
        return res.status(404).json({ error: "Person not found" });
      })
      .catch((err) => {
        console.error(err);
        return res.status(500).json({ error: "Database error" });
      });
  }
});

// Create a new person
app.post("/api/persons", (req, res) => {
  const { name } = req.body;
  if (!name) {
    return res.status(400).json({ error: "Invalid data" });
  }
  db.one("INSERT INTO Persons (name) VALUES ($1) RETURNING *", [name])
    .then((result) => {
      return res.status(201).json(result);
    })
    .catch((err) => {
      console.error(err);
      return res.status(500).json({ error: "Database error" });
    });
});

// Update a person by ID or Name
app.put("/api/persons/:param", (req, res) => {
  const param = req.params.param;

  if (!isNaN(param)) {
    // If param is numeric, assume it's an ID
    const personId = parseInt(param);
    const { name } = req.body;
    if (!name) {
      return res.status(400).json({ error: "Invalid data" });
    }
    db.oneOrNone("UPDATE Persons SET name = $1 WHERE id = $2 RETURNING *", [name, personId])
      .then((result) => {
        if (result) {
          return res.json(result);
        }
        return res.status(404).json({ error: "Person not found" });
      })
      .catch((err) => {
        console.error(err);
        return res.status(500).json({ error: "Database error" });
      });
  } else {
    // If param is not numeric, assume it's a Name
    const { name: newName } = req.body;
    if (!newName) {
      return res.status(400).json({ error: "Invalid data" });
    }
    db.oneOrNone("UPDATE Persons SET name = $1 WHERE name = $2 RETURNING *", [newName, param])
      .then((result) => {
        if (result) {
          return res.json(result);
        }
        return res.status(404).json({ error: "Person not found" });
      })
      .catch((err) => {
        console.error(err);
        return res.status(500).json({ error: "Database error" });
      });
  }
});

// Delete a person by ID or Name
app.delete("/api/persons/:param", (req, res) => {
  const param = req.params.param;

  if (!isNaN(param)) {
    // If param is numeric, assume it's an ID
    const personId = parseInt(param);
    db.none("DELETE FROM Persons WHERE id = $1", [personId])
      .then(() => {
        return res.json({ message: "Person deleted" });
      })
      .catch((err) => {
        console.error(err);
        return res.status(500).json({ error: "Database error" });
      });
  } else {
    // If param is not numeric, assume it's a Name
    db.none("DELETE FROM Persons WHERE name = $1", [param])
      .then(() => {
        return res.json({ message: "Person deleted" });
      })
      .catch((err) => {
        console.error(err);
        return res.status(500).json({ error: "Database error" });
      });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

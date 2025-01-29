import React, { useState } from "react";
import { loginUser } from "./authService"; // Adjust the path as necessary
import { useNavigate } from "react-router-dom";
import { Card, Form, Button, Alert } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const Login = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(null); // Clear any previous error messages
    try {
      const userData = await loginUser(email, password); // Assume loginUser sends credentials to backend and returns user data
      if (userData && userData.token) {
        // Pass the user data to the onLogin function in App.js
        onLogin(userData);
        navigate("/dashboard"); // Navigate to the dashboard on successful login
      }
    } catch (err) {
      // Handle login errors and display appropriate messages
      setError(err.message || "Invalid credentials or server error");
    }
  };

  return (
    <div
      className="d-flex justify-content-center align-items-center vh-100"
      style={{ backgroundColor: "#eef2f3" }}
    >
      <Card style={{ width: "22rem" }} className="shadow-sm">
        <Card.Body>
          <h3 className="text-center mb-4">Login</h3>
          {error && <Alert variant="danger">{error}</Alert>}
          <Form onSubmit={handleLogin}>
            <Form.Group className="mb-3" controlId="formEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                style={{
                  borderRadius: "8px",
                  boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
                }}
              />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                style={{
                  borderRadius: "8px",
                  boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
                }}
              />
            </Form.Group>
            <div className="d-grid">
              <Button
                type="submit"
                variant="primary"
                style={{
                  borderRadius: "8px",
                  backgroundColor: "#007bff",
                  border: "none",
                  boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.2)",
                }}
              >
                Login
              </Button>
            </div>
          </Form>
        </Card.Body>
      </Card>
    </div>
  );
};

export default Login;

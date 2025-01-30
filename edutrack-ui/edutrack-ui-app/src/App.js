import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import Dashboard from "./components/Dashboard";
import AddRole from "./components/AddRole";
import StudentManagement from "./components/StudentManagement";
import AuthContext from "./components/AuthContext";
import BatchManagement from "./components/BatchManagement";
import CourseManagement from "./components/CourseManagement";

const App = () => {
  const [user, setUser] = useState(null); // To store user info including role
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Fetch user role from the backend
  const fetchUserRole = async (storedUser) => {
    try {
      const response = await fetch("http://localhost:5000/auth/user-role", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${storedUser.token}`, // Include token for authorization
        },
      });
      
      const roleData = await response.json(); // Parse response only once
      if (!response.ok) {
        throw new Error("Failed to fetch user role");
      }
      return roleData.role; // Return the fetched role
    } catch (error) {
      console.error("Error fetching user role:", error);
      return null; // Return null if fetching fails
    }
  };

  // Handle user login and fetch role
  const handleLogin = async (userData) => {
    try {
      const role = await fetchUserRole(userData); // Fetch user role after login
      if (role) {
        const updatedUser = { ...userData, role }; // Add role to user data
        setUser(updatedUser);
        setIsAuthenticated(true);
        localStorage.setItem("user", JSON.stringify(updatedUser)); // Store updated user in localStorage
      } else {
        alert("Failed to fetch user role. Please try again.");
      }
    } catch (error) {
      console.error("Error during login:", error);
    }
  };

  // Handle user logout
  const handleLogout = () => {
    setUser(null);
    setIsAuthenticated(false);
    localStorage.removeItem("user"); // Remove user data from localStorage
  };

  // Check authentication status and validate role on page load
  useEffect(() => {
    const storedUser = JSON.parse(localStorage.getItem("user"));
    if (storedUser) {
      fetchUserRole(storedUser).then((role) => {
        if (role) {
          setUser({ ...storedUser, role });
          setIsAuthenticated(true);
        } else {
          handleLogout(); // Log out if role validation fails
        }
      });
    }
  }, []);

  return (
    <AuthContext.Provider value={{ user, isAuthenticated, handleLogout }}>
      <Router>
        <Routes>
          {!isAuthenticated ? (
            <>
              <Route path="/login" element={<Login onLogin={handleLogin} />} />
              <Route path="*" element={<Navigate to="/login" />} />
            </>
          ) : (
            <>
              <Route path="/dashboard" element={<Dashboard />} />
              {user.role === "hr" && (
                <>
                  <Route path="/register" element={<Register />} />
                  <Route path="/addrole" element={<AddRole />} />
                </>
              )}
              <Route path="/studentmanagement" element={<StudentManagement />} />
              <Route path="/batchmanagement" element={<BatchManagement />} />
              <Route path="/coursemanagement" element={<CourseManagement />} />


              <Route path="*" element={<Navigate to="/dashboard" />} />
            </>
          )}
        </Routes>
      </Router>
    </AuthContext.Provider>
  );
};

export default App;

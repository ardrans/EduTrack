import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import AddRole from './components/AddRole';
import StudentManagement from './components/StudentManagement';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/addrole" element={<AddRole />} />
        <Route path="/studentmanagement" element={<StudentManagement />} />


      </Routes>
    </Router>
  );
}

export default App;

import React, { useContext } from 'react';
import { Container, Nav } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import AuthContext from './AuthContext';

function Dashboard() {
  const { user, handleLogout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogoutClick = () => {
    handleLogout();
    navigate('/login');
  };

  const sidebarStyle = {
    height: '100vh',
    position: 'fixed',
    backgroundColor: '#343a40',
    color: '#fff',
    padding: '20px',
    width: '250px',
  };

  const contentStyle = {
    marginLeft: '270px',
    padding: '20px',
    textAlign: 'center',
  };

  const navLinkStyle = {
    color: '#fff',
    textDecoration: 'none',
    margin: '10px 0',
    display: 'block',
  };

  return (
    <div>
      {/* Sidebar Navigation */}
      <div style={sidebarStyle}>
        <h3 className="text-center">EduTrack</h3>
        <Nav className="flex-column">
          <Link to="/" style={navLinkStyle}>Home</Link>
          {user?.role === 'hr' && (
            <>
              <Link to="/studentmanagement" style={navLinkStyle}>Student Management</Link>
              <Link to="/addrole" style={navLinkStyle}>Add Role</Link>
              <Link to="/register" style={navLinkStyle}>Register</Link>
            </>
          )}
          <Link to="/dashboard" style={navLinkStyle}>Dashboard</Link>
          <button
            className="btn btn-danger mt-3"
            onClick={handleLogoutClick}
            style={{ width: '100%' }}
          >
            Logout
          </button>
        </Nav>
      </div>

      {/* Main Content */}
      <div style={contentStyle}>
        <h1>Welcome to EduTrack</h1>
        <p>Your centralized platform for managing educational activities.</p>
      </div>
    </div>
  );
}

export default Dashboard;

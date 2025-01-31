import React, { useContext, useState, useEffect } from 'react';
import { Container, Nav, Card } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import AuthContext from './AuthContext';
import { getTrainersCount, getStudents } from './authService';
import { getBatches } from './BatchService';
import backgroundImage from './images/geometric-science-education-background-vector-gradient-blue-digital-remix_53876-125993.avif';

function Dashboard() {
  const { user, handleLogout } = useContext(AuthContext);
  const navigate = useNavigate();

  const [trainersCount, setTrainersCount] = useState(0);
  const [studentsCount, setStudentsCount] = useState(0);
  const [batchesCount, setBatchesCount] = useState(0);

  const handleLogoutClick = () => {
    handleLogout();
    navigate('/login');
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const trainersData = await getTrainersCount();
        const studentsData = await getStudents();
        const batchesData = await getBatches();

        animateCount(trainersData.trainers_count, setTrainersCount);
        animateCount(studentsData.total_students, setStudentsCount);
        animateCount(batchesData.total_batches, setBatchesCount);
      } catch (error) {
        console.error('Error fetching counts:', error);
      }
    };
    fetchData();
  }, []);

  const animateCount = (target, setter) => {
    let count = 0;
    const interval = setInterval(() => {
      count++;
      setter(count);
      if (count >= target) clearInterval(interval);
    }, 50);
  };

  const containerStyle = {
    minHeight: '100vh',
    backgroundImage: `url(${backgroundImage})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
  };

  return (
    <div style={containerStyle} className="d-flex">
      {/* Sidebar Navigation */}
      <div style={{ height: '100vh', position: 'fixed', backgroundColor: '#343a40', color: '#fff', padding: '20px', width: '250px' }}>
        <h3 className="text-center">EduTrack</h3>
        <Nav className="flex-column">
          <Link to="/" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Home</Link>
          {user?.role === 'hr' && (
            <>
              <Link to="/studentmanagement" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Student Management</Link>
              <Link to="/batchmanagement" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Batch Management</Link>
              <Link to="/coursemanagement" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Course Management</Link>
              <Link to="/topicmanagement" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Topic Management</Link>
              <Link to="/addrole" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Add Role</Link>
              <Link to="/register" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Register</Link>
            </>
          )}
          <Link to="/dashboard" style={{ color: '#fff', textDecoration: 'none', margin: '10px 0', display: 'block' }}>Dashboard</Link>
          <button className="btn btn-danger mt-3" onClick={handleLogoutClick} style={{ width: '100%' }}>Logout</button>
        </Nav>
      </div>

      {/* Main Content */}
      <div style={{ marginLeft: '270px', padding: '20px', textAlign: 'center', flex: 1 }}>
        <h1 className="display-4" style={{color:'white'}}>EduTrack Dashboard</h1>
        <p className="lead" style={{color:'white'}}>Manage your educational activities efficiently</p>
        
        {/* Displaying Counts */}
        <div className="counts-section d-flex justify-content-center gap-4 mt-4">
          <Card className="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center" style={{ width: '100px', height: '100px', fontSize: '20px' }}>{trainersCount}</Card>
          <Card className="rounded-circle bg-success text-white d-flex align-items-center justify-content-center" style={{ width: '100px', height: '100px', fontSize: '20px' }}>{studentsCount}</Card>
          <Card className="rounded-circle bg-warning text-dark d-flex align-items-center justify-content-center" style={{ width: '100px', height: '100px', fontSize: '20px' }}>{batchesCount}</Card>
        </div>
      </div>

      {/* Side Panel for Tech News and Placement Drives */}
      <div style={{ width: '300px', padding: '20px', backgroundColor: 'transparent', borderLeft: '1px solid #ccc', minHeight: '100vh' }}>
        <h4 className="text-center mb-3" style={{color:'white',fontSize:'30px'}}>Latest Updates</h4>
        <Card className="mb-3 p-3" style={{backgroundColor:'transparent'}}>
          <h5 style={{color:'white'}}>Technology News</h5>
          <ul style={{color:'white'}}>
            <li>React 19 Beta released with new features</li>
            <li>Python 3.13 preview available for developers</li>
            <li>AI advancements in web development</li>
          </ul>
        </Card>
        <Card className="p-3" style={{backgroundColor:'transparent'}}>
          <h5 style={{color:'white'}}>Upcoming Placement Drives</h5>
          <ul style={{color:'white'}}>
            <li>Google hiring event - 20th July</li>
            <li>Infosys virtual drive - 25th July</li>
            <li>TCS campus placement - 1st August</li>
          </ul>
        </Card>
      </div>
    </div>
  );
}

export default Dashboard;

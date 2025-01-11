import React, { useState, useEffect } from 'react';
import { createUserWithRole } from './authService';

const Dashboard = () => {
    const [users, setUsers] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('');

    useEffect(() => {
        // Fetch existing users (you can implement this API in Flask backend)
    }, []);

    const handleAddUser = async (e) => {
        e.preventDefault();
        try {
            const data = { name, email, password, role_id: role };
            const response = await createUserWithRole(data);
            if (response && response.user) {
                setUsers([...users, response.user]);
            }
        } catch (error) {
            console.error('Error adding user:', error);
        }
    };

    return (
        <div>
            <h2>Admin Dashboard</h2>
            <h3>Add User</h3>
            <form onSubmit={handleAddUser}>
                <input
                    type="text"
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Role"
                    value={role}
                    onChange={(e) => setRole(e.target.value)}
                />
                <button type="submit">Add User</button>
            </form>

            <h3>Users</h3>
            <ul>
                {users.map((user) => (
                    <li key={user.id}>
                        {user.name} - {user.email} - {user.role_id}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;

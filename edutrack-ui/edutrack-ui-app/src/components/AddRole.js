import React, { useState } from 'react';
import { addRole } from './authService';  

const AddRole = () => {
    const [roleName, setRoleName] = useState('');
    const [message, setMessage] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!roleName) {
            setMessage('Role name is required!');
            return;
        }

        setLoading(true);
        try {
            const response = await addRole(roleName);
            setMessage(response.message || 'Role added successfully');
            setRoleName('');  // Reset input field after successful submission
        } catch (error) {
            setMessage(error.response?.data?.error || 'Error adding role');
        }
        setLoading(false);
    };

    return (
        <div style={{ margin: '2rem', padding: '1rem', border: '1px solid #ccc', borderRadius: '8px' }}>
            <h2>Add Role</h2>
            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '1rem' }}>
                    <label htmlFor="roleName" style={{ display: 'block', marginBottom: '0.5rem' }}>Role Name:</label>
                    <input
                        type="text"
                        id="roleName"
                        value={roleName}
                        onChange={(e) => setRoleName(e.target.value)}
                        placeholder="Enter role name"
                        style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #ccc' }}
                    />
                </div>
                <button
                    type="submit"
                    disabled={loading}
                    style={{
                        backgroundColor: '#007bff',
                        color: '#fff',
                        padding: '0.5rem 1rem',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: loading ? 'not-allowed' : 'pointer',
                    }}
                >
                    {loading ? 'Adding...' : 'Add Role'}
                </button>
            </form>
            {message && (
                <p style={{ marginTop: '1rem', color: message.includes('successfully') ? 'green' : 'red' }}>
                    {message}
                </p>
            )}
        </div>
    );
};

export default AddRole;

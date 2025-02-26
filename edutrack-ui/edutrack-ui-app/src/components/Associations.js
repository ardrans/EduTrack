import React, { useEffect, useState } from 'react';
import { getAllAssociations, deleteAssociation, createAssociation  } from './AssociationService';
import { Table, Button, Form, Container, Alert, Spinner } from 'react-bootstrap';

const BatchAllocation = () => {
    const [allocations, setAllocations] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [batchName, setBatchName] = useState('');
    const [studentEmail, setStudentEmail] = useState('');

    useEffect(() => {
        fetchAllocations();
    }, []);

    const fetchAllocations = async () => {
        try {
            const data = await getAllAssociations();
            setAllocations(data.batches);
            setLoading(false);
        } catch (err) {
            setError('Error fetching batch allocations');
            setLoading(false);
        }
    };

    const handleCreate = async (e) => {
        e.preventDefault();
        try {
            await createAssociation({ batch_name: batchName, student_email: studentEmail });
            setBatchName('');
            setStudentEmail('');
            fetchAllocations();
        } catch (err) {
            setError('Error creating batch allocation');
        }
    };

    const handleDelete = async (id) => {
        if (window.confirm('Are you sure you want to remove this allocation?')) {
            try {
                await deleteAssociation(id);
                fetchAllocations();
            } catch (err) {
                setError('Error deleting batch allocation');
            }
        }
    };

    return (
        <Container className="mt-4">
            <h2 className="text-center mb-4">Batch Allocation</h2>
            {error && <Alert variant="danger">{error}</Alert>}
            
            {/* Add Allocation Form */}
            <Form onSubmit={handleCreate} className="mb-4">
                <Form.Group className="mb-3">
                    <Form.Control
                        type="text"
                        placeholder="Batch Name"
                        value={batchName}
                        onChange={(e) => setBatchName(e.target.value)}
                        required
                    />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control
                        type="email"
                        placeholder="Student Email"
                        value={studentEmail}
                        onChange={(e) => setStudentEmail(e.target.value)}
                        required
                    />
                </Form.Group>
                <Button variant="primary" type="submit">Add Allocation</Button>
            </Form>

            {/* Loading Spinner */}
            {loading && <div className="text-center"><Spinner animation="border" /></div>}
            
            {/* Allocations Table */}
            {!loading && (
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Batch Name</th>
                            <th>Student Count</th>
                            <th>Student Name</th>
                            <th>Student Email</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {Object.entries(allocations).map(([batch, students]) => (
                            students.map((student, index) => (
                                <tr key={student.id}>
                                    {index === 0 && <td rowSpan={students.length}>{batch}</td>}
                                    {index === 0 && <td rowSpan={students.length}>{students.length}</td>}
                                    <td>{student.name}</td>
                                    <td>{student.email}</td>
                                    <td>
                                        <Button variant="danger" onClick={() => handleDelete(student.id)}>Remove</Button>
                                    </td>
                                </tr>
                            ))
                        ))}
                    </tbody>
                </Table>
            )}
        </Container>
    );
};

export default BatchAllocation;

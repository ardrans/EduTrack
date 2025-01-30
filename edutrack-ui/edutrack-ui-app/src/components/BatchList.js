import React from 'react';
import { Table, Button } from 'react-bootstrap';

const BatchList = ({ batches, onEdit, onDelete, onViewDetails }) => {
    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {batches.map((batch) => (
                    <tr key={batch.id}>
                        <td>{batch.id}</td>
                        <td>{batch.name}</td>
                        <td>{batch.start_date}</td>
                        <td>{batch.end_date}</td>
                        <td>
                            <Button variant="info" onClick={() => onViewDetails(batch.id)}>View Details</Button>{' '}
                            <Button variant="warning" onClick={() => onEdit(batch)}>Edit</Button>{' '}
                            <Button variant="danger" onClick={() => onDelete(batch.id)}>Delete</Button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
};

export default BatchList;

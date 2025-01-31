import React from 'react';
import { Table, Button } from 'react-bootstrap';

const TopicList = ({ topics, onEdit, onDelete, onViewDetails }) => {
    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Content</th>
                    <th>Course ID</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {topics.map(topic => (
                    <tr key={topic.id}>
                        <td>{topic.id}</td>
                        <td>{topic.name}</td>
                        <td>{topic.description}</td>
                        <td>{topic.course_id}</td>
                        <td>
                            <Button variant="info" onClick={() => onViewDetails(topic.id)} className="me-2">View</Button>
                            <Button variant="warning" onClick={() => onEdit(topic)} className="me-2">Edit</Button>
                            <Button variant="danger" onClick={() => onDelete(topic.id)}>Delete</Button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
};

export default TopicList;
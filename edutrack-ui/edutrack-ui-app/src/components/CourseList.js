import React from 'react';
import { Table, Button } from 'react-bootstrap';

const CourseList = ({ courses, onEdit, onDelete }) => {
    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Course Name</th>
                    <th>Description</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {courses.length > 0 ? (
                    courses.map((course, index) => (
                        <tr key={course.id}>
                            <td>{index + 1}</td>
                            <td>{course.name}</td>
                            <td>{course.description}</td>
                            <td>
                                <Button variant="warning" onClick={() => onEdit(course)} className="me-2">
                                    Edit
                                </Button>
                                <Button variant="danger" onClick={() => onDelete(course.id)}>
                                    Delete
                                </Button>
                            </td>
                        </tr>
                    ))
                ) : (
                    <tr>
                        <td colSpan="4" className="text-center">No courses available</td>
                    </tr>
                )}
            </tbody>
        </Table>
    );
};

export default CourseList;

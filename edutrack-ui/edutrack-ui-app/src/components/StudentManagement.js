import React, { useEffect, useState } from 'react';
import { getStudents, createStudent, updateStudent, deleteStudent } from './authService';
import StudentForm from './StudentForm';
import StudentList from './StudentList';
import { Container, Button, Card } from 'react-bootstrap';

const StudentManagement = () => {
    const [students, setStudents] = useState([]);
    const [editingStudent, setEditingStudent] = useState(null);
    const [showForm, setShowForm] = useState(false); // State to toggle form view

    useEffect(() => {
        fetchStudents();
    }, []);

    const fetchStudents = async () => {
        const data = await getStudents();
        setStudents(data.students);
    };

    const handleCreateOrUpdate = async (data) => {
        console.log("Submitting data:", data); // Log form data
        if (editingStudent) {
            await updateStudent(editingStudent.id, data);
        } else {
            await createStudent(data);
        }
        setEditingStudent(null);
        setShowForm(false); // Return to list view
        fetchStudents();
    };

    const handleDelete = async (id) => {
        await deleteStudent(id);
        fetchStudents();
    };

    const handleEdit = (student) => {
        setEditingStudent(student);
        setShowForm(true); // Show form for editing
    };

    const handleAddNew = () => {
        setEditingStudent(null); // Reset editing state
        setShowForm(true); // Show form for adding
    };

    return (
        <Container>
            <h1 className="text-center my-4">Student Management</h1>
            {showForm ? (
                <Card className="p-4 mb-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                    <Button 
                        variant="secondary" 
                        onClick={() => setShowForm(false)} 
                        style={{ marginBottom: '15px' }}
                    >
                        Back to List
                    </Button>
                    <StudentForm onSubmit={handleCreateOrUpdate} student={editingStudent} />
                </Card>
            ) : (
                <div>
                    <Button 
                        variant="primary" 
                        onClick={handleAddNew} 
                        className="mb-4"
                    >
                        Add New Student
                    </Button>
                    <Card className="p-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                        <StudentList
                            students={students}
                            onEdit={handleEdit}
                            onDelete={handleDelete}
                        />
                    </Card>
                </div>
            )}
        </Container>
    );
};

export default StudentManagement;

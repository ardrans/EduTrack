import React, { useEffect, useState } from 'react';
import { getStudents, createStudent, updateStudent, deleteStudent } from './authService';
import StudentForm from './StudentForm';
import StudentList from './StudentList';
import { Container, Button, Card } from 'react-bootstrap';

const StudentManagement = () => {
    const [students, setStudents] = useState([]);
    const [editingStudent, setEditingStudent] = useState(null);
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
        fetchStudents();
    }, []);

    const fetchStudents = async () => {
        const data = await getStudents();
        setStudents(data.students);
    };

    const handleCreateOrUpdate = async (data) => {
        console.log("Submitting data:", data);
        if (editingStudent) {
            await updateStudent(editingStudent.id, data);
        } else {
            await createStudent(data);
        }
        setEditingStudent(null);
        setShowForm(false);
        fetchStudents();
    };

    const handleDelete = async (id) => {
        await deleteStudent(id);
        fetchStudents();
    };

    const handleEdit = (student) => {
        setEditingStudent(student);
        setShowForm(true);
    };

    const handleAddNew = () => {
        setEditingStudent(null);
        setShowForm(true);
    };

    // **Handle "Placed" checkbox toggle**
    const handleTogglePlaced = async (id) => {
        const student = students.find((s) => s.id === id);
        if (student) {
            await updateStudent(id, { placed: !student.placed }); // Toggle the "placed" status
            fetchStudents(); // Refresh student list
        }
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
                            onTogglePlaced={handleTogglePlaced} // Pass the function to StudentList
                        />
                    </Card>
                </div>
            )}
        </Container>
    );
};

export default StudentManagement;

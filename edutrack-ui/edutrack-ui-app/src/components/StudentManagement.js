import React, { useEffect, useState } from 'react';
import { getStudents, createStudent, updateStudent, deleteStudent } from './authService';
import StudentForm from './StudentForm';
import StudentList from './StudentList';

const StudentManagement = () => {
    const [students, setStudents] = useState([]);
    const [editingStudent, setEditingStudent] = useState(null);

    useEffect(() => {
        fetchStudents();
    }, []);

    const fetchStudents = async () => {
        const data = await getStudents();
        setStudents(data);
    };

    const handleCreateOrUpdate = async (data) => {
        if (editingStudent) {
            await updateStudent(editingStudent.id, data);
        } else {
            await createStudent(data);
        }
        setEditingStudent(null);
        fetchStudents();
    };

    const handleDelete = async (id) => {
        await deleteStudent(id);
        fetchStudents();
    };

    const handleEdit = (student) => {
        setEditingStudent(student);
    };

    return (
        <div>
            <h1>Student Management</h1>
            <StudentForm onSubmit={handleCreateOrUpdate} student={editingStudent} />
            <StudentList
                students={students}
                onEdit={handleEdit}
                onDelete={handleDelete}
            />
        </div>
    );
};

export default StudentManagement;

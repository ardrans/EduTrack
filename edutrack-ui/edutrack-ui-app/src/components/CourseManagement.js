import React, { useEffect, useState } from 'react';
import { getCourses, createCourse, updateCourse, deleteCourse } from './CourseService';
import CourseForm from './CourseForm';
import CourseList from './CourseList';
import { Container, Button, Card } from 'react-bootstrap';

const CourseManagement = () => {
    const [courses, setCourses] = useState([]);
    const [editingCourse, setEditingCourse] = useState(null);
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
        fetchCourses();
    }, []);

    const fetchCourses = async () => {
        const data = await getCourses();
        setCourses(data);
    };

    const handleCreateOrUpdate = async (data) => {
        console.log("Submitting data:", data);
        if (editingCourse) {
            await updateCourse(editingCourse.id, data);
        } else {
            await createCourse(data);
        }
        setEditingCourse(null);
        setShowForm(false);
        fetchCourses();
    };

    const handleDelete = async (id) => {
        await deleteCourse(id);
        fetchCourses();
    };

    const handleEdit = (course) => {
        setEditingCourse(course);
        setShowForm(true);
    };

    const handleAddNew = () => {
        setEditingCourse(null);
        setShowForm(true);
    };

    return (
        <Container>
            <h1 className="text-center my-4">Course Management</h1>
            {showForm ? (
                <Card className="p-4 mb-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                    <Button 
                        variant="secondary" 
                        onClick={() => setShowForm(false)} 
                        style={{ marginBottom: '15px' }}
                    >
                        Back to List
                    </Button>
                    <CourseForm onSubmit={handleCreateOrUpdate} course={editingCourse} />
                </Card>
            ) : (
                <div>
                    <Button 
                        variant="primary" 
                        onClick={handleAddNew} 
                        className="mb-4"
                    >
                        Add New Course
                    </Button>
                    <Card className="p-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                        <CourseList
                            courses={courses}
                            onEdit={handleEdit}
                            onDelete={handleDelete}
                        />
                    </Card>
                </div>
            )}
        </Container>
    );
};

export default CourseManagement;
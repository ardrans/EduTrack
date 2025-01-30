import React, { useState, useEffect } from 'react';
import { Form, Button } from 'react-bootstrap';
import { getCourses, getTrainers } from './BatchService'

const BatchForm = ({ onSubmit, batch, onCancel }) => {
    const [formData, setFormData] = useState({
        name: '',
        start_date: '',
        end_date: '',
        trainer_id: '',
        course_id: ''
    });

    const [trainers, setTrainers] = useState([]);
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const fetchedCourses = await getCourses();
                setCourses(fetchedCourses);

                const fetchedTrainers = await getTrainers();
                setTrainers(fetchedTrainers);
            } catch (error) {
                console.error("Error fetching courses or trainers:", error);
            }
        };

        fetchData();
    }, []);

    useEffect(() => {
        if (batch) {
            setFormData({
                name: batch.name,
                start_date: batch.start_date,
                end_date: batch.end_date,
                trainer_id: batch.trainer_id || '',
                course_id: batch.course_id || ''
            });
        }
    }, [batch]);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    const isDateValid = formData.end_date >= formData.start_date;

    return (
        <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
                <Form.Label>Name</Form.Label>
                <Form.Control 
                    type="text" 
                    name="name" 
                    value={formData.name} 
                    onChange={handleChange} 
                    required 
                />
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Start Date</Form.Label>
                <Form.Control 
                    type="date" 
                    name="start_date" 
                    value={formData.start_date} 
                    onChange={handleChange} 
                    required 
                />
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>End Date</Form.Label>
                <Form.Control 
                    type="date" 
                    name="end_date" 
                    value={formData.end_date} 
                    onChange={handleChange} 
                    required 
                />
                {formData.end_date && formData.start_date && !isDateValid && (
                    <div className="text-danger mt-2">End Date cannot be before Start Date</div>
                )}
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Course</Form.Label>
                <Form.Select 
                    name="course_id" 
                    value={formData.course_id} 
                    onChange={handleChange} 
                    required
                >
                    <option value="">Select Course</option>
                    {courses.map((course) => (
                        <option key={course.id} value={course.id}>
                            {course.name}
                        </option>
                    ))}
                </Form.Select>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Trainer</Form.Label>
                <Form.Select 
                    name="trainer_id" 
                    value={formData.trainer_id} 
                    onChange={handleChange} 
                    required
                >
                    <option value="">Select Trainer</option>
                    {trainers.map((trainer) => (
                        <option key={trainer.id} value={trainer.id}>
                            {trainer.name}
                        </option>
                    ))}
                </Form.Select>
            </Form.Group>

            <Button variant="primary" type="submit" disabled={!isDateValid}>
                {batch ? 'Update Batch' : 'Create Batch'}
            </Button>

            {onCancel && (
                <Button variant="secondary" onClick={onCancel} style={{ marginLeft: '10px' }}>
                    Cancel
                </Button>
            )}
        </Form>
    );
};

export default BatchForm;

import React, { useEffect, useState } from 'react';
import { getTopics, createTopic, updateTopic, deleteTopic, getTopic } from './TopicService';
import TopicForm from './TopicForm';
import TopicList from './TopicList';
import { Container, Button, Card } from 'react-bootstrap';

const TopicManagement = () => {
    const [topics, setTopics] = useState([]);
    const [editingTopic, setEditingTopic] = useState(null);
    const [showForm, setShowForm] = useState(false);
    const [topicDetails, setTopicDetails] = useState(null);

    useEffect(() => {
        fetchTopics();
    }, []);

    const fetchTopics = async () => {
        const data = await getTopics();
        setTopics(data);
    };

    const handleCreateOrUpdate = async (data) => {
        if (editingTopic) {
            await updateTopic(editingTopic.id, data);
        } else {
            await createTopic(data);
        }
        setEditingTopic(null);
        setShowForm(false);
        fetchTopics();
    };

    const handleDelete = async (id) => {
        await deleteTopic(id);
        fetchTopics();
    };

    const handleEdit = (topic) => {
        setEditingTopic(topic);
        setShowForm(true);
    };

    const handleAddNew = () => {
        setEditingTopic(null);
        setShowForm(true);
    };

    const handleViewDetails = async (topicId) => {
        const data = await getTopic(topicId);
        setTopicDetails(data);
    };

    return (
        <Container>
            <h1 className="text-center my-4">Topic Management</h1>
            {showForm ? (
                <Card className="p-4 mb-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                    <Button variant="secondary" onClick={() => setShowForm(false)} style={{ marginBottom: '15px' }}>
                        Back to List
                    </Button>
                    <TopicForm onSubmit={handleCreateOrUpdate} topic={editingTopic} />
                </Card>
            ) : (
                <div>
                    <Button variant="primary" onClick={handleAddNew} className="mb-4">
                        Add New Topic
                    </Button>
                    <Card className="p-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                        <TopicList
                            topics={topics}
                            onEdit={handleEdit}
                            onDelete={handleDelete}
                            onViewDetails={handleViewDetails}
                        />
                    </Card>
                </div>
            )}

            {topicDetails && (
                <Card className="mt-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                    <Card.Body>
                        <h3>Topic Details</h3>
                        <p><strong>Title:</strong> {topicDetails.title}</p>
                        <p><strong>Content:</strong> {topicDetails.content}</p>
                        <p><strong>Course:</strong> {topicDetails.course ? topicDetails.course.name : 'Not assigned'}</p>
                    </Card.Body>
                </Card>
            )}
        </Container>
    );
};

export default TopicManagement;

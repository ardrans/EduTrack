import React, { useEffect, useState } from 'react';
import { getBatches, createBatch, updateBatch, deleteBatch, getBatch } from './BatchService';
import BatchForm from './BatchForm';
import BatchList from './BatchList';
import { Container, Button, Card, Modal } from 'react-bootstrap';

const BatchManagement = () => {
    const [batches, setBatches] = useState([]);
    const [editingBatch, setEditingBatch] = useState(null);
    const [showForm, setShowForm] = useState(false);
    const [batchDetails, setBatchDetails] = useState(null);
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        fetchBatches();
    }, []);

    const fetchBatches = async () => {
        const data = await getBatches();
        setBatches(data.batches);
    };

    const handleCreateOrUpdate = async (data) => {
        if (editingBatch) {
            await updateBatch(editingBatch.id, data);
        } else {
            await createBatch(data);
        }
        setEditingBatch(null);
        setShowForm(false);
        fetchBatches();
    };

    const handleDelete = async (id) => {
        await deleteBatch(id);
        fetchBatches();
    };

    const handleEdit = (batch) => {
        setEditingBatch(batch);
        setShowForm(true);
    };

    const handleAddNew = () => {
        setEditingBatch(null);
        setShowForm(true);
    };

    const handleViewDetails = async (batchId) => {
        const data = await getBatch(batchId);
        setBatchDetails(data);
        setShowModal(true);
    };

    return (
        <Container>
            <h1 className="text-center my-4">Batch Management</h1>
            {showForm ? (
                <Card className="p-4 mb-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                    <Button 
                        variant="secondary" 
                        onClick={() => setShowForm(false)} 
                        style={{ marginBottom: '15px' }}
                    >
                        Back to List
                    </Button>
                    <BatchForm onSubmit={handleCreateOrUpdate} batch={editingBatch} />
                </Card>
            ) : (
                <div>
                    <Button 
                        variant="primary" 
                        onClick={handleAddNew} 
                        className="mb-4"
                    >
                        Add New Batch
                    </Button>
                    <Card className="p-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
                        <BatchList
                            batches={batches}
                            onEdit={handleEdit}
                            onDelete={handleDelete}
                            onViewDetails={handleViewDetails}
                        />
                    </Card>
                </div>
            )}

            {/* Batch Details Modal */}
            <Modal show={showModal} onHide={() => setShowModal(false)} centered>
                <Modal.Header closeButton>
                    <Modal.Title>Batch Details</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    {batchDetails && (
                        <>
                            <p><strong>Name:</strong> {batchDetails.name}</p>
                            <p><strong>Start Date:</strong> {new Date(batchDetails.start_date).toLocaleDateString()}</p>
                            <p><strong>End Date:</strong> {new Date(batchDetails.end_date).toLocaleDateString()}</p>
                            <p><strong>Student Count:</strong> {batchDetails.student_count}</p>
                            <p><strong>Trainer:</strong> {batchDetails.trainer ? batchDetails.trainer.name : 'Not assigned'}</p>
                            <h5>Topics:</h5>
                            <ul>
                                {batchDetails.topics && batchDetails.topics.map((topic, index) => (
                                    <li key={index}>{topic.name}</li>
                                ))}
                            </ul>
                        </>
                    )}
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={() => setShowModal(false)}>Close</Button>
                </Modal.Footer>
            </Modal>
        </Container>
    );
};

export default BatchManagement;

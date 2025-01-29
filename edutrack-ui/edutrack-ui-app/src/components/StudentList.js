import React from 'react';

const StudentList = ({ students, onEdit, onDelete }) => (
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Profile Picture</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {students.map((student) => (
                <tr key={student.id}>
                    <td>{student.name}</td>
                    <td>{student.email}</td>
                    <td>{student.phone}</td>
                    <td>
                        {student.profile_picture ? (
                            <img
                                src={student.profile_picture}
                                alt={student.name}
                                width="50"
                            />
                        ) : (
                            'N/A'
                        )}
                    </td>
                    <td>
                        <button onClick={() => onEdit(student)}>Edit</button>
                        <button onClick={() => onDelete(student.id)}>Delete</button>

                    </td>
                </tr>
            ))}
        </tbody>
    </table>
);

export default StudentList;

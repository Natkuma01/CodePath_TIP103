import { useState, useEffect } from 'react';

function Snorlax() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetch(){
            try{
                const response = await fetch('http://www.google.com');
                if (!response.ok) {
                    throw new Error(`http status: ${response.status}`)
                }
                const data = await response.json()
                setUser(data)
            } catch (error) {
                setError(error.message)
            } finally {
                setLoading(false)
            }
        }
        fetch()
    }, [])

    if (loading) return <p> Loading right now...do not rush me</p>
    if (error) return <p>Error: {error}</p>

    return (
        <ul>
            {users.map(user => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ul>
    )
}
import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { FaUser, FaLock } from "react-icons/fa";
import { useUser } from '../Usercontext'; // Import the useUser hook

const LoginForm = () => {
    const [msg, setMsg] = useState('');
    const navigate = useNavigate();
    const { setUser } = useUser(); // Access setUser method from the UserContext
    const [formData, setFormData] = useState({
        username: '',
        password: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/login', formData);
            
            if (response.status === 200 && response.data.data) {
                console.log("200");
                const { user_id, user_type, user_name } = response.data.data;
                console.log(user_id, user_type, user_name);
                setUser(user_id, user_type, user_name); // Set user data globally
                if (user_type === "Patient") {
                    navigate("/patientdashboard");
                } else {
                    navigate("/admindashboard");
                }
            } else {
                const { msg } = response.data; // Corrected this line
                setMsg(msg); // Set the message in the state
            }
        } catch (error) {
            console.error('Error:', error);
            setMsg('An error occurred during login. Please try again.');
        }
    };

    return (
        <div id="authentication-page">
            <div className="container">
                <div className="row col-lg-10 auth-row offset-lg-1 marg-left round-corner">
                    <div className="col-lg-6">
                        <div className="col-md-12">
                            <h3>Welcome to <h2 className="highlight-h2">Dentalease</h2></h3>
                            <p className="tagline">Your one-stop destination for hassle-free dental appointments.</p>
                        </div>
                        <img src="img/dentists-treating-patients-teeth-in-the-clinic-vector.jpg" className="img-responsive img-fix-hgt" alt="" />
                    </div>
                    <div className="col-lg-6 form-div right-side-round-corner">
                        <div className="auth-wrapper">
                            <form onSubmit={handleSubmit} method="post">
                                <h2 className="highlight-h2">Login</h2>
                                <div className="input-box">
                                    <input type="text" name="username" id="username" value={formData.username} onChange={handleChange} placeholder="Username" required/>
                                    <FaUser className="icon" />
                                </div>
                                <div className="input-box">
                                    <input type="password" name="password" id="password" value={formData.password} onChange={handleChange} placeholder="Password" required />
                                    <FaLock className="icon" />
                                </div>
                                {msg && <p className="error-message">{msg}</p>}
                                <div className="forgot-password">
                                    <a href="/forgot-password">Forgot Password?</a>
                                </div>

                                <button className="btn btn-custom btn-lg" type="submit">Login</button>

                                <div className="register-link">
                                    <p>Don't have an account? <a href="/register">Register</a></p>
                                </div>                
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default LoginForm;

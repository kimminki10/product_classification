import React from 'react';
import AuthForm from '../components/auth/AuthForm';
import AuthTemplate from '../components/auth/authTemplate';

const RegisterPage = () => {
    return (
        <AuthTemplate>
            <AuthForm type="register"/>
        </AuthTemplate>
    )
};

export default RegisterPage;
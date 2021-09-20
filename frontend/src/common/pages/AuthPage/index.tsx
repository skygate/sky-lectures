import { useLocation } from 'react-router-dom';

import { PageWrapper, AuthWrapper, AuthPageImg } from './styles';

import RegisterForm from 'common/components/AuthPageComponents/RegisterForm';
import LoginForm from 'common/components/AuthPageComponents/LoginForm';
import AuthPageImage from 'assets/images/auth-page-img.svg';

const AuthPage = () => {
  const currentUrl = useLocation();

  return (
    <PageWrapper>
      <AuthWrapper>
        {currentUrl.pathname === '/register' ? <RegisterForm /> : <LoginForm />}
      </AuthWrapper>
      <AuthPageImg src={AuthPageImage} />
    </PageWrapper>
  );
};

export default AuthPage;

import { PageWrapper, AuthWrapper, AuthPageImg } from './styles';

import LoginForm from 'common/components/AuthPageComponents/LoginForm';
import AuthPageImage from 'assets/images/auth-page-img.svg';

const AuthPage = () => {
  return (
    <PageWrapper>
      <AuthWrapper>
        <LoginForm />
      </AuthWrapper>
      <AuthPageImg src={AuthPageImage} />
    </PageWrapper>
  );
};

export default AuthPage;

import { PageWrapper, AuthPageImg } from './styles';

import AuthPageImage from 'assets/images/auth-page-img.svg';

const AuthPage = () => {
  return (
    <PageWrapper>
      Login
      <AuthPageImg src={AuthPageImage} />
    </PageWrapper>
  );
};

export default AuthPage;

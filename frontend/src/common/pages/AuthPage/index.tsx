import * as S from './styles';

import RegisterAndLogin from 'common/components/RegisterAndLogin';
import AuthPageImage from 'assets/images/auth-page-img.svg';

const AuthPage = () => {
  return (
    <S.PageWrapper>
      <S.AuthWrapper>
        <RegisterAndLogin />
      </S.AuthWrapper>
      <S.AuthPageImgWrapper>
        <S.AuthPageImg src={AuthPageImage} />
      </S.AuthPageImgWrapper>
    </S.PageWrapper>
  );
};

export default AuthPage;

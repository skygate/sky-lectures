import { useState } from 'react';
import { useLocation } from 'react-router';
import { Formik } from 'formik';

import * as S from './styles';
import EyePasswordIcon from 'assets/images/eye-password-icon.svg';

const RegisterAndLogin = () => {
  const [isPasswordHidden, setIsPasswordHidden] = useState(true);

  const currentUrl = useLocation();
  const isRegisterPage = currentUrl.pathname === '/register';

  const togglePasswordVisibility = () => {
    setIsPasswordHidden(isPasswordHidden => !isPasswordHidden);
  };

  return (
    <S.FormWrapper>
      <S.FormHeading>{isRegisterPage ? `Let's get started!` : 'Hello!'}</S.FormHeading>
      <S.FormSubheading>
        {isRegisterPage ? `It's a pleasure to meet you` : `Let's study`}
      </S.FormSubheading>
      <Formik
        initialValues={
          isRegisterPage
            ? { login: '', email: '', password: '' }
            : {
                login: '',
                password: '',
              }
        }
        onSubmit={values => {
          //There is gonna be a request
          console.log('Sending request...');
        }}
      >
        {formik => (
          <S.InputFieldWrapper onSubmit={formik.handleSubmit}>
            <S.InputField name="login" type="text" placeholder="login" />
            {isRegisterPage && <S.InputField name="email" type="email" placeholder="email" />}
            <S.PasswordInputFieldWrapper>
              <S.InputField
                name="password"
                type={isPasswordHidden ? 'password' : 'test'}
                placeholder="password"
              />
              <S.PasswordIcon src={EyePasswordIcon} onClick={() => togglePasswordVisibility()} />
            </S.PasswordInputFieldWrapper>
            <S.SubmitButton type="submit">{isRegisterPage ? 'Sign up' : 'Sign in'}</S.SubmitButton>
          </S.InputFieldWrapper>
        )}
      </Formik>
      <S.RedirectWrapper>
        <S.RedirectMessage>
          {isRegisterPage ? 'Already have an account?' : `Don't have an account yet?`}
        </S.RedirectMessage>
        <S.RedirectButton to={isRegisterPage ? '/login' : '/register'}>Sign up</S.RedirectButton>
      </S.RedirectWrapper>
    </S.FormWrapper>
  );
};

export default RegisterAndLogin;

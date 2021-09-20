import { Formik } from 'formik';

import * as S from '../styles';

const LoginForm = () => {
  return (
    <S.FormWrapper>
      <S.FormHeading>Hello!</S.FormHeading>
      <S.FormSubheading>Let's study</S.FormSubheading>
      <Formik
        initialValues={{
          login: '',
          password: '',
        }}
        onSubmit={values => {
          console.log('Sending request...');
        }}
      >
        {formik => (
          <S.InputFieldWrapper onSubmit={formik.handleSubmit}>
            <S.InputField name="login" type="text" placeholder="login" />
            <S.InputField name="password" type="password" placeholder="password" />
            <S.SubmitButton type="submit">Sign in</S.SubmitButton>
          </S.InputFieldWrapper>
        )}
      </Formik>
      <S.RedirectWrapper>
        <S.RedirectMessage>Don't have an account yet?</S.RedirectMessage>
        <S.RedirectButton to="/register">Sign up</S.RedirectButton>
      </S.RedirectWrapper>
    </S.FormWrapper>
  );
};

export default LoginForm;

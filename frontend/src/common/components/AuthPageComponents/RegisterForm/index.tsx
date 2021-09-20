import { Formik } from 'formik';

import * as S from '../styles';

const RegisterForm = () => {
  return (
    <S.FormWrapper>
      <S.FormHeading>Let's get started!</S.FormHeading>
      <S.FormSubheading>It's pleasure to meet you</S.FormSubheading>
      <Formik
        initialValues={{
          login: '',
          email: '',
          password: '',
        }}
        onSubmit={values => {
          //There is gonna be be a request
          console.log('Sending request...');
        }}
      >
        {formik => (
          <S.InputFieldWrapper onSubmit={formik.handleSubmit}>
            <S.InputField name="login" type="text" placeholder="login" />
            <S.InputField name="email" type="e-mail" placeholder="e-mail" />
            <S.InputField name="password" type="password" placeholder="password" />
            <S.SubmitButton type="submit">Sign up</S.SubmitButton>
          </S.InputFieldWrapper>
        )}
      </Formik>
      <S.RedirectWrapper>
        <S.RedirectMessage>Already have an account?</S.RedirectMessage>
        <S.RedirectButton to="/login">Sign up</S.RedirectButton>
      </S.RedirectWrapper>
    </S.FormWrapper>
  );
};

export default RegisterForm;

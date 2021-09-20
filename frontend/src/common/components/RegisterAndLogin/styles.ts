import styled from 'styled-components';
import { fontSize, colors, fontWeight } from 'config/stylesConfig';

import { Form, Field } from 'formik';
import { Link } from 'react-router-dom';
import SVG from 'react-inlinesvg';

export const FormWrapper = styled.div`
  position: relative;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
`;

export const FormHeading = styled.h1`
  font-size: ${fontSize.extraLarge};
  color: ${colors.darkMain};
  margin-bottom: 10px;
`;

export const FormSubheading = styled.span`
  font-size: ${fontSize.medium};
  color: ${colors.darkMain};
  margin-bottom: 15px;
`;

export const InputFieldWrapper = styled(Form)`
  display: flex;
  flex-direction: column;
`;

export const InputField = styled(Field)`
  outline: none;

  height: 50px;
  width: 350px;
  display: flex;
  margin: 5px 0px;
  padding: 5px 45px 5px 30px;
  background: ${colors.white};
  border: 1px solid ${colors.border};
  border-radius: 25px;
`;

export const SubmitButton = styled.button`
  border: none;
  outline: none;
  cursor: pointer;

  height: 50px;
  width: 350px;
  margin-top: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: ${colors.darkMain};
  font-size: ${fontSize.normal};
  letter-spacing: 0.05em;
  font-weight: ${fontWeight.medium};
  color: ${colors.white};
  border-radius: 25px;
`;

export const RedirectWrapper = styled.div`
  display: flex;
  margin-top: 15px;
`;

export const RedirectMessage = styled.span`
  font-size: ${fontSize.small};
  font-weight: ${fontWeight.extraMedium};
  color: ${colors.lightMain};
  letter-spacing: 0.03em;
`;

export const RedirectButton = styled(Link)`
  text-decoration: none;

  margin-left: 15px;
  font-size: ${fontSize.small};
  font-weight: ${fontWeight.extraMedium};
  color: ${colors.darkMain};
  letter-spacing: 0.03em;
`;

export const PasswordInputFieldWrapper = styled.div`
  position: relative;
`;

export const PasswordIcon = styled(SVG)`
  position: absolute;
  left: 90%;
  margin-top: -35px;
`;

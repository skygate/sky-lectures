import styled from 'styled-components';

import SVG from 'react-inlinesvg';
import { colors } from 'config/stylesConfig';

export const PageWrapper = styled.div`
  min-height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  font-family: 'Roboto', sans-serif;
`;

export const AuthWrapper = styled.div`
  min-height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const AuthPageImgWrapper = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
`;

export const AuthPageImg = styled(SVG)`
  width: 95%;
  height: 95%;
  border-radius: 20px;
  background-color: ${colors.darkMain};
`;

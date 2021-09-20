import styled from 'styled-components';

import SVG from 'react-inlinesvg';

export const PageWrapper = styled.div`
  height: 100vh;
  display: flex;
  align-items: center;
  font-family: 'Roboto', sans-serif;
`;

export const AuthWrapper = styled.div`
  height: 100vh;
  width: 50vw;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const AuthPageImg = styled(SVG)`
  width: 50vw;
  height: 90%;
`;

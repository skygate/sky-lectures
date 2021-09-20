import { createGlobalStyle } from 'styled-components';

export const GlobalStyles = createGlobalStyle`
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;

        @font-face {
            font-family: 'Roboto';
            src: url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        }
    }
`;

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Routes } from 'config/variables';

import AuthPage from 'common/pages/AuthPage';

const AppRoutes = () => {
  return (
    <Router>
      <Switch>
        <Route path={[Routes.register, Routes.login]} exact component={AuthPage} />
      </Switch>
    </Router>
  );
};

export default AppRoutes;

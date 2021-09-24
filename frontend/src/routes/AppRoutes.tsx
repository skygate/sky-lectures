import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Routes } from 'config/variables';

import AuthPage from 'common/pages/AuthPage';
import NotFoundPage from 'common/pages/NotFoundPage';

const AppRoutes = () => {
  return (
    <Router>
      <Switch>
        <Route path={[Routes.register, Routes.login]} exact component={AuthPage} />
        <Route path="*" exact component={NotFoundPage} />
      </Switch>
    </Router>
  );
};

export default AppRoutes;

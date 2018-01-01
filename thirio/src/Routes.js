import React from 'react'
import { Route, Switch } from 'react-router-dom'
import Home from './containers/Home/Home'
import NotFound from './containers/NotFound/NotFound'

export default () => {
  return (
    <Switch>
      <Route path="/" exact component={Home} />
      <Route component={NotFound} />
    </Switch>
  )
}

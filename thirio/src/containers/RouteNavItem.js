import React from 'react'
import { Route } from 'react-router-dom'
import { Menu } from 'semantic-ui-react'

export default props => {
  return (
    <Route
      path={props.href}
      exact
      children={({match, history}) => {
        console.log(match)
        return (
          <Menu secondary>
            <Menu.Item
              href={props.href}
              name={props.children}
              onClick={e => history.push(e.currentTarget.getAttribute("href"))}
              active = {match ? true : false}
              {...props}
            />
          </Menu>
        )
      }}
    >

    </Route>
  )
}

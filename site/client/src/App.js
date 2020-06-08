import React, { Component } from "react";
import { Box, Button, Heading, Collapsible, Grommet } from 'grommet';
import { Notification } from 'grommet-icons';

const theme = {
    global: {
      colors: {
        brand: '#228BE6'
      },
      font: {
        family: 'Roboto',
        size: '18px',
        height: '20px',
      },
    },
  };

  const AppBar = (props) => (
    <Box
      tag='header'
      direction='row'
      align='center'
      justify='between'
      background='brand'
      pad={{ left: 'medium', right: 'small', vertical: 'small' }}
      elevation='medium'
      style={{ zIndex: '1' }}
      {...props}
    />
  );

class App extends Component {


    constructor(props) {
        super(props);
        this.state = {
            apiResponse: "",
            dbResponse: "",
            showSidebar: false
        };
    }

    // Go to API and check testAPI route for a response
    callAPI() {
        fetch("/testAPI")
            .then(res => res.text())
            .then(res => this.setState({ apiResponse: res }))
            .catch(err => err);
    }

    // Go to API and check testDB route for a response
    callDB() {
        fetch("/testDB")
            .then(res => res.text())
            .then(res => this.setState({ dbResponse: res }))
            .catch(err => err);
    }

    // Execute the calls when componnent mounts
    componentDidMount() {
        this.callAPI();
        this.callDB();
    }

    render() {
        return (
            <Grommet theme={theme} full>
              <Box fill>
                <AppBar>
                  <Heading level='3' margin='none'>My App</Heading>
                  <Button 
                    icon={<Notification />} 
                    onClick={() => this.setState({showSidebar: !this.state.showSidebar})} 
                  />
                </AppBar>
                <Box direction='row' flex overflow={{ horizontal: 'hidden' }}>
                  <Collapsible direction="horizontal" open={this.state.showSidebar}>
                    <Box
                      flex
                      width='medium'
                      background='light-2'
                      elevation='small'
                      align='center'
                      justify='center'
                    >
                      sidebar
                    </Box>
                  </Collapsible>
                  <Box flex align='center' justify='center'>
                    app body
                  </Box>
                </Box>
                <p className="App-intro">{this.state.apiResponse}</p>
                <p className="App-intro">{this.state.dbResponse}</p>
              </Box>
            </Grommet>
        );
    }
}

export default App;

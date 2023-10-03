import { ChakraProvider, Tabs, TabList, TabPanels, Tab, TabPanel } from '@chakra-ui/react';
import React from 'react';
import theme from '../../theme';

const Nav = () =>{
 return(
    <ChakraProvider theme={theme}>
        <Tabs variant='soft-rounded' colorScheme='green'>
  <TabList>
    <Tab>Saved</Tab>
    <Tab>Search</Tab>
  </TabList>
  <TabPanels>
    <TabPanel>
      <p>Database</p>
    </TabPanel>
    <TabPanel>
      <p>Web Scrapper</p>
    </TabPanel>
  </TabPanels>
</Tabs>
    </ChakraProvider>
 );   
};

export default Nav;
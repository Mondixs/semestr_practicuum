import { Container, Row, Col } from 'react-bootstrap';
import AddContactForm from '../components/AddContactForm';
import ContactList from '../components/ContactList';
import { useState } from 'react';


// Определяем интерфейс Contact
interface Contact {
  id: number;
  name: string;
  phoneNumber: string;
}

const HomePage = () => {
  const [contacts, setContacts] = useState<Contact[]>([]);

  const addContact = (name: string, phoneNumber: string) => {
    setContacts([...contacts, { id: Date.now(), name, phoneNumber }]);
  };

  const deleteContact = (id: number) => {
    setContacts(contacts.filter((contact) => contact.id !== id));
  };

  return (
    <Container>
      <Row className="mt-5">
        <Col md={{ span: 6, offset: 3 }}>
          <h1>Записная книжка</h1>
          <AddContactForm onSubmit={addContact} />
          <ContactList contacts={contacts} onDelete={deleteContact} />
        </Col>
      </Row>
    </Container>
  );
};

export default HomePage;
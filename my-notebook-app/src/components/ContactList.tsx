import { ListGroup } from 'react-bootstrap';

interface Contact {
  id: number;
  name: string;
  phoneNumber: string;
}

interface ContactListProps {
  contacts: Contact[];
  onDelete: (id: number) => void;
}

const ContactList = ({ contacts, onDelete }: ContactListProps) => {
  if (!contacts.length) {
    return <p>Контакты отсутствуют.</p>;
  }

  return (
    <ListGroup>
      {contacts.map((contact) => (
        <ListGroup.Item key={contact.id}>
          <strong>{contact.name}</strong>: {contact.phoneNumber}{' '}
          <button onClick={() => onDelete(contact.id)}>Удалить</button>
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default ContactList;
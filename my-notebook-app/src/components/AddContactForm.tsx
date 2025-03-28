import { Form, Button } from 'react-bootstrap';
import { useState } from 'react';

interface AddContactFormProps {
  onSubmit: (name: string, phoneNumber: string) => void;
}

const AddContactForm = ({ onSubmit }: AddContactFormProps) => {
  const [name, setName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    onSubmit(name, phoneNumber);
    setName('');
    setPhoneNumber('');
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formBasicName">
        <Form.Label>Имя</Form.Label>
        <Form.Control 
          type="text"
          placeholder="Введите имя"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="formBasicPhoneNumber">
        <Form.Label>Номер телефона</Form.Label>
        <Form.Control
          type="tel"
          placeholder="Введите номер телефона"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
        />
      </Form.Group>

      <Button variant="primary" type="submit">
        Добавить контакт
      </Button>
    </Form>
  );
};

export default AddContactForm;
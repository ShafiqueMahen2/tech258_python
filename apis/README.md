# Tech 258 - APIs

## What are APIs? How are they used and why are they so popular?
An API (Application Programming Interface) is a way for two or more computer programs or components to communicate with one another. APIs are used to share data between these systems using a request and response cycle. APIs are popular as they allow this communication to occur in real-time and over the internet.

![Alt text](/images/API_data_transfer.png "API Data Transfer Diagram")

## What is a REST API? what makes an API RESTful? What are the REST API guidelines?
A REST API is an architectural style for an API that conforms to the constraints of REST (Representational State Transfer). An API is RESTful when it uses HTTP requests to access and use data. This data is then used to GET, PUT, POST and DELETE data types, referring to the reading, updating, creating and deleting of operations concerning resources. The REST API also adheres to the guidelines below:

- **Stateless Operations**: Each request from a client to a server is treated as an isolated transaction.
- **Client-Server Architecture**: There is a clear distinction between clients and servers.#
- **Cacheable Responses**: Must specify if a response can be cached.
- **Layered**: Components are arranged in layers with each layer having a specific set of responsibilities.
- **Uniform Interface**: To ensure a consistent set of interactions.

## What is HTTP? (What does it stand for? What is HTTPS?)
HTTP (HyperText Transfer Protocol) is the foundation of the World Wide Web, designed to transfer information between networked devices. It is an application layer protocol and runs on top of other layers in the network protocol stack.

HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP.

## Explain HTTP request structure using the diagrams provided, or your own (see attachments)

The common HTTP request structure may contain the following components:

- **VERB** (method): This component indicates the action that the client wants to perform on the server e.g. GET, POST, PUT, DELETE, etc.
- **URL**: This component specifies the location of the resource being requested. It could be a path or a full URL (examples):
```
/example/resource
https://www.example.com/example/resource
```
- **Version**: Indicates the version of the HTTP protocol being used e.g. HTTP/1.1, HTTP/2.
- **Header**: Contains additional information about the request, stored in a Key-Value pair format, where the key is the header name and the value is its corresponding value.
- **Body**: Contains any additional data that the client wants to send to the server.

![Alt text](/images/HTTP_request_structure.png "HTTP Request Structure Diagram")

## Explain HTTP response structure using the diagrams provided, or your own (see attachments)
The common HTTP response structure may contain the following components:

- **Response Code**: This code indicates the status of the response, the most common response codes include:
    1) 1xx: Informational response.
    2) 2xx: Success response e.g. 200 OK
    3) 3xx: Redirection responses e.g. 301 Moved Permanently
    4) 4xx: Client error responses e.g. 404 Not Found
    5) 5xx: Server error responses e.g. 500 Internal Server Error
- **Version**: Indicates the version of the HTTP protocol being used e.g. HTTP/1.1, HTTP/2.
- **Header**: Contains additional information about the response, stored in a Key-Value pair format, where the key is the header name and the value is its corresponding value.
- **Body**: Contains the actual content returned by the server e.g. HTML content or JSON data.

![Alt text](/images/HTTP_response_structure.png "HTTP Request Structure Diagram")

## What are the 5 HTTP verbs? And what does each do?
These are the 5 HTTP verbs, these verbs correspond to CRUD (Create, Read, Update, Delete) operations:

- **POST**: Submits data to the server. (Create operation).
- **GET**: Retrieves a single or list of items from the server. (Read operation).
- **PATCH**: Partially modifying an item on the server. (Update operation).
- **DELETE**: Deletes an item from the server. (Delete operation).
- **PUT**: Updates or replaces an existing item on the server. (Create/Replace operation).

## What is "statelessness"? Show some examples of "stateless" http requests and then a few "stateful" http requests.
Statelessness refers to the principle that each request from a client to the server must contain all the necessary information to fulfill said request, without relying on any previous interactions stored on the server, (no client session state between requests).

A Stateless Protocol adheres to this, by not requiring the server to retain session information or information about each communicating partner for single/multiple requests. Examples being a GET request for a web page or a GET request for user information from the server.

A Stateful Protocol does not adhere to this principle as it may require additional information from the server. If this is not given, the request may need to be resent. Examples: User Authentication (Server may have to provide additional information e.g. status, session token, etc.), Shopping Cart Interaction (Server may have to maintain state of shopping cart).

![Alt text](/images/rest_api_stateful_vs_stateless.png "REST API: Stateful vs Stateless")

## What is caching?
Caching is the process of storing copies of files in a cache (temporary storage location), so they can be accessed quickly. In the context of web applcations, caching may be useful to serve future requests more quickly as it happens at various different levels e.g. Client-side caching and Server-side caching.


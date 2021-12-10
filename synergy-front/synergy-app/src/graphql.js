import gql from 'graphql-tag'

export const GET_OCCUPATIONS = gql`
query {
  occupations{id, name, companyName, positionName,
    hireDate, fireDate, salary, fraction, base, advance, advance, byHours}
}
`
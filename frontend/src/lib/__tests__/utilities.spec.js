import * as utils from '../utilities'

const obj = {
  firstName: '',
  lastName: undefined,
  email: null,
  address: null,
  phone: null,
  birthday: null,
}

const address = {
  country: null,
  city: null,
  street: null,
  houseNumber: null,
}

describe('isAllEmptyFields', () => {
  it('returns true when all fields are empty', () => {
    expect(utils.isAllEmptyFields(obj)).toBe(true)
  })

  it('returns false when one field is not empty', () => {
    expect(utils.isAllEmptyFields({...obj, email: 'email@email.com'})).toBe(
      false
    )
  })

  describe('when one field is object', () => {
    const newObj = {...obj, address}
    it('returns true if all fields are empty', () => {
      expect(utils.isAllEmptyFields(newObj)).toBe(true)
    })

    it('returns false if one field is not empty', () => {
      newObj.address.city = 'City'
      expect(utils.isAllEmptyFields(newObj)).toBe(false)

      newObj.phone = 856421324
      newObj.address.city = null
      expect(utils.isAllEmptyFields(newObj)).toBe(false)
    })
  })
})

describe('stringToPascalCase', () => {
  const test = 'test test test'
  const snakeCase = 'test_test'
  const stringWithSymbols = '$test&test#test@test%test^test'
  const stringWithDash = 'test-test-test'
  const stringWithPunctuation = 'test,:; .test'

  describe('return string is concatenated, and every first letter of the word is uppercase', () => {
    describe('when a string with spaces', () => {
      it('return string is TestTestTest', () => {
        expect(utils.stringToPascalCase(test)).toBe('TestTestTest')
      })
    })

    describe('when camelcase', () => {
      it('return string is TestTest', () => {
        expect(utils.stringToPascalCase(snakeCase)).toBe('TestTest')
      })
    })

    describe('when symbols are used', () => {
      it('return string is TestTestTestTestTestTest', () => {
        expect(utils.stringToPascalCase(stringWithSymbols)).toBe(
          'TestTestTestTestTestTest'
        )
      })
    })

    describe('when a dash is used', () => {
      it('return string is TestTestTest', () => {
        expect(utils.stringToPascalCase(stringWithDash)).toBe('TestTestTest')
      })
    })

    describe('when a punctuation string', () => {
      it('return string is TestTest', () => {
        expect(utils.stringToPascalCase(stringWithPunctuation)).toBe('TestTest')
      })
    })
  })
})

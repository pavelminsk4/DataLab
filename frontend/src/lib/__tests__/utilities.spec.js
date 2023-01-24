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

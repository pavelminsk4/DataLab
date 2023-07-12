import {SORT_BY} from '@lib/constants'

export default {
  data() {
    return {
      sortBy: {
        property: '',
        condition: '',
      },
    }
  },
  computed: {
    tableValue() {
      if (!this.sortBy.property) return this.widgetData

      const ratio = this.sortBy.condition === SORT_BY.DESCENDING ? -1 : 1

      if (this.sortBy.property === 'date') {
        return [...this.widgetData].sort(
          (a, b) =>
            ratio *
            (new Date(b[this.sortBy.property]) -
              new Date(a[this.sortBy.property]))
        )
      }

      return [...this.widgetData].sort((a, b) => {
        const firstValue = a[this.sortBy.property]
        const secondValue = b[this.sortBy.property]

        if (typeof firstValue === 'number' && typeof secondValue === 'number') {
          return ratio * (secondValue - firstValue)
        }
        if (typeof firstValue === 'string' && typeof secondValue === 'string') {
          let result = 0
          const firstStringLowerCase = firstValue.toLowerCase()
          const secondStringLowerCase = secondValue.toLowerCase()

          if (firstStringLowerCase < secondStringLowerCase) result = -1
          if (firstStringLowerCase > secondStringLowerCase) result = 1

          return ratio * result
        }

        return 0
      })
    },
  },
  methods: {
    sorting(property, condition) {
      this.sortBy = {property, condition}
    },
  },
}

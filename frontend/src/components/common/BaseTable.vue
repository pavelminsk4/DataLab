<template>
  <table :class="['base-table', hasMinWidth && 'min-width']">
    <thead>
      <tr>
        <th v-if="hasCheckbox" style="width: 60px">
          <BaseCheckbox v-if="hasSelectAll" v-model="isCheckedAllProxy" />
        </th>
        <th
          v-for="item in tableHeader"
          :key="`header-${item.name}`"
          :style="item.width && `width: ${item.width};`"
          @click="() => sortingBy(item)"
        >
          <div class="header-container">
            <component v-if="item.hasIcon" :is="`${item.iconName}Icon`" />
            <CustomText tag="span" :text="capitalizeFirstLetter(item.name)" />
            <SortArrowIcon
              v-if="item.hasSort"
              :sort-by="sortBy[item.sortProperty]"
            />
          </div>
        </th>
        <th v-if="hasCheckbox && hasActions" style="width: 80px">
          <CustomText text="Actions" />
        </th>
      </tr>
    </thead>
    <tbody>
      <slot></slot>
    </tbody>
  </table>
</template>

<script>
import {capitalizeFirstLetter} from '@lib/utilities'
import {SORT_BY} from '@lib/constants'

import CustomText from '@/components/CustomText'
import BaseCheckbox from '@/components/BaseCheckbox2'
import SortArrowIcon from '@/components/icons/SortArrowIcon'
import MostActiveAuthorIcon from '../icons/MostActiveAuthorIcon'
import MostInfluentialAuthorIcon from '../icons/MostInfluentialAuthorIcon'

const {ASCENDING, DESCENDING} = SORT_BY

export default {
  name: 'BaseTable',
  components: {
    CustomText,
    BaseCheckbox,
    SortArrowIcon,
    MostActiveAuthorIcon,
    MostInfluentialAuthorIcon,
  },
  props: {
    tableHeader: {type: Array, required: true},
    hasCheckbox: {type: Boolean, default: true},
    hasActions: {type: Boolean, default: true},
    hasSelectAll: {type: Boolean, default: true},
    hasMinWidth: {type: Boolean, default: false},
  },
  data() {
    return {
      isCheckedAll: false,
      sortBy: {},
    }
  },
  computed: {
    isCheckedAllProxy: {
      get() {
        return this.isCheckedAll
      },
      set(val) {
        this.isCheckedAll = val
        this.$emit('select-all', this.isCheckedAll)
      },
      windowWidth() {
        return window.innerWidth
      },
    },
  },
  created() {
    this.tableHeader.forEach((column) => {
      this.sortBy[column.sortProperty] = column.isDefaultSort ? ASCENDING : ''
    })
  },
  methods: {
    capitalizeFirstLetter,
    sortingBy({sortProperty, hasSort}) {
      if (!hasSort) return

      switch (this.sortBy[sortProperty]) {
        case ASCENDING:
          this.sortBy[sortProperty] = DESCENDING
          break
        default:
          this.sortBy = {}
          this.sortBy[sortProperty] = ASCENDING
          break
      }

      this.$emit('sorting-by', sortProperty, this.sortBy[sortProperty])
    },
  },
}
</script>

<style lang="scss">
.base-table {
  width: 100%;

  border-collapse: separate;
  border-spacing: 0;

  cursor: pointer;

  thead {
    tr {
      th {
        padding: 8px 16px;

        vertical-align: middle;
        text-align: left;
        font-weight: 500;
        font-size: 11px;

        .header-container {
          display: flex;
          align-items: center;
        }
      }
    }
  }

  tbody {
    tr {
      background: var(--background-secondary-color);

      &:hover {
        z-index: 2;

        filter: drop-shadow(0px 21px 21px rgba(113, 93, 231, 0.09))
          drop-shadow(0px 5px 11px rgba(113, 93, 231, 0.1))
          drop-shadow(0px 0px 0px rgba(113, 93, 231, 0.1));
      }

      td {
        padding: 16px;

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        word-break: break-word;
      }
    }
  }

  .td_name {
    font-weight: 600;
  }
}

.min-width {
  @media (max-width: 1170px) {
    width: 1200px;
  }
}
</style>

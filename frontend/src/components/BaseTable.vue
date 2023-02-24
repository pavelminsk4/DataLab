<template>
  <table class="base-table">
    <thead>
      <tr>
        <th style="width: 60px">
          <BaseCheckbox v-model="isSelectAllProxy" />
        </th>
        <th
          v-for="item in tableHeader"
          :key="`header-${item.name}`"
          :style="item.width && `width: ${item.width};`"
        >
          {{ capitalizeFirstLetter(item.name) }}
        </th>
        <th style="width: 80px">Actions</th>
      </tr>
    </thead>
    <tbody>
      <slot></slot>
    </tbody>
  </table>
</template>

<script>
import {capitalizeFirstLetter} from '@lib/utilities'
import BaseCheckbox from '@/components/BaseCheckbox2'

export default {
  name: 'BaseTable',
  components: {
    BaseCheckbox,
  },
  props: {
    tableHeader: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      isSelectAll: false,
    }
  },
  computed: {
    isSelectAllProxy: {
      get() {
        return this.isSelectAll
      },
      set(val) {
        this.isSelectAll = val
        this.$emit('select-all', this.isSelectAll)
      },
    },
  },
  methods: {
    capitalizeFirstLetter,
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

        text-align: left;
        font-weight: 500;
        font-size: 11px;
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
</style>

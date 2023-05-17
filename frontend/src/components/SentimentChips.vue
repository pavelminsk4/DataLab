<template>
  <div class="container" @click="openDropdown">
    <BaseChips :chips-type="chipsType" />
    <ul v-if="isOpen" :id="`dropdown-${postId}`" class="dropdown">
      <li
        v-for="option in options"
        :value="option"
        :key="option"
        class="dropdown__item"
        @click="closeDropdown"
      >
        {{ option }}
      </li>
    </ul>
  </div>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import BaseChips from '@/components/BaseChips'

export default {
  name: 'SentimentChips',
  components: {BaseChips},
  props: {
    chipsType: {type: String, required: true},
    postId: {type: [String, Number], required: true},
  },
  data() {
    return {
      isOpen: false,
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
  },
  created() {
    this.dropdownStyles =
      'top: auto; bottom: 25px; background-color: var(--background-secondary-color);'
    this.options = ['Negative', 'Neutral', 'Positive']
    // document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.removeEventListener('click', this.closeDropdown)
  },
  methods: {
    ...mapActions([action.CHANGE_POST_SENTIMENT]),
    openDropdown() {
      this.isOpen = !this.isOpen
    },

    closeDropdown({target}) {
      const dropdownList = document.getElementById(`dropdown-${this.postId}`)

      if (!dropdownList?.contains(target)) {
        this.isOpenDropdown = false
      }
    },
    changePostSentiment() {
      this[action.CHANGE_POST_SENTIMENT]({
        postId: this.postId,
        departmentId: this.department.id,
        newSentiment: 'neutral',
      })
    },
  },
}
</script>

<style type="scss">
.container {
  display: flex;

  cursor: pointer;

  .dropdown {
    position: absolute;

    padding: 10px;

    background: var(--background-secondary-color);
    box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);
    border-radius: 8px;

    list-style: none;
  }
}
</style>

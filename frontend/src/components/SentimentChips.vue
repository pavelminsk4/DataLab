<template>
  <div class="container" :id="`dropdown-${postId}`" @click="openDropdown">
    <BaseChips :chips-type="newType || chipsType" :id="`chips-${postId}`" />
    <ul v-if="isOpen" class="dropdown">
      <li
        v-for="option in options"
        :key="option"
        class="dropdown__item"
        @click="changePostSentiment"
      >
        <BaseChips
          :chips-type="option.toLowerCase()"
          style="background-color: var(--background-secondary-color)"
        />
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
      newType: '',
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
  },
  created() {
    this.options = ['Negative', 'Neutral', 'Positive']
    document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.removeEventListener('click', this.closeDropdown)
  },
  methods: {
    ...mapActions([
      action.CHANGE_ONLINE_POST_SENTIMENT,
      action.CHANGE_SOCIAL_POST_SENTIMENT,
    ]),
    openDropdown() {
      this.isOpen = !this.isOpen
    },

    closeDropdown({target}) {
      const dropdownList = document.getElementById(`dropdown-${this.postId}`)
      if (!dropdownList) return

      if (!dropdownList?.contains(target)) {
        this.isOpen = false
      }
    },

    async changePostSentiment({currentTarget}) {
      const newSentiment = currentTarget.innerText.toLowerCase()

      const {name} = this.$route
      let moduleName = 'SOCIAL'
      if (name.includes('Online')) moduleName = 'ONLINE'

      const request = await this[action[`CHANGE_${moduleName}_POST_SENTIMENT`]](
        {
          postId: this.postId,
          departmentId: this.department.id,
          newSentiment,
        }
      )
      if (request instanceof Error) {
        return
      } else this.newType = newSentiment
    },
  },
}
</script>

<style lang="scss">
.container {
  display: flex;

  position: relative;

  cursor: pointer;

  .dropdown {
    position: absolute;

    margin-top: 35px;
    padding: 10px;

    background: var(--background-secondary-color);
    box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);
    border-radius: 8px;

    list-style: none;
  }
}
</style>

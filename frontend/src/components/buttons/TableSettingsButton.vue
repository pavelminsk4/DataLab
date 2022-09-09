<template>
  <div class="settings-container" ref="settings-wrapper">
    <div v-if="isOpenElement" class="options-container">
      <div class="option">
        <FolderIcon />
        Move to
      </div>
      <div class="option">
        <DuplicateIcon />
        Duplicate
      </div>
      <div class="option">
        <DeleteIcon />
        Delete
      </div>
    </div>
    <PointsIcon class="points-icon" @click="openSettings" />
  </div>
</template>

<script>
import PointsIcon from '@components/icons/PointsIcon'
import FolderIcon from '@components/icons/FolderIcon'
import DuplicateIcon from '@components/icons/DuplicateIcon'
import DeleteIcon from '@components/icons/DeleteIcon'

export default {
  name: 'TableSettingsButton',
  components: {
    DeleteIcon,
    DuplicateIcon,
    FolderIcon,
    PointsIcon,
  },
  props: {
    id: {
      type: [Number, String],
      default: '',
    },
  },
  data() {
    return {
      isOpenElement: false,
    }
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    openSettings() {
      this.isOpenElement = !this.isOpenElement
    },
    close() {
      const elements = document.querySelectorAll('.settings-container')

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
        this.isOpenElement = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-container {
  position: relative;
}

.options-container {
  position: absolute;
  bottom: 32px;
  right: 0;

  display: flex;
  flex-direction: column;

  border-radius: 15px;
  padding: 17px 29px 18px 22px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.22);

  color: black;
  background: #ffffff;
}

.close-options {
  display: none;
}

.option {
  display: flex;
  align-items: center;

  svg {
    width: 20px;
    height: 20px;

    margin-right: 10px;
  }
}

.points-icon {
  margin-right: 17px;

  flex-shrink: 0;

  color: var(--secondary-text-color);

  transition: all 0.3s;
}

.points-icon:hover {
  border-radius: 100%;

  color: var(--primary-text-color);
  background-color: var(--primary-button-color);
}
</style>
